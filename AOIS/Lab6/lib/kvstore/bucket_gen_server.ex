defmodule KVStore.BucketGenServer do
  use GenServer

  # Public interface

  def start_link(options \\ []) do
    GenServer.start_link(__MODULE__, :ok, options)
  end

  def get(bucket, key) do
    GenServer.call(bucket, {:get, key})
  end

  def list(bucket) do
    GenServer.call(bucket, :list)
  end

  def put(bucket, key, value) do
    GenServer.cast(bucket, {:put, key, value})
  end

  def delete(bucket, key) do
    GenServer.call(bucket, {:delete, key})
  end

  def stop(bucket, reason \\ :normal) do
    GenServer.stop(bucket, reason)
  end

  # Server callbacks

  def init(:ok) do
    {:ok, %{len: 0, cap: 5, items: %{}}}
  end

  def handle_call(:list, _from, %{items: items} = state) do
    {:reply, items, state}
  end

  def handle_call({:get, key}, _from, %{items: items, cap: cap} = state) do
    hashed_key = hash_key(key, cap)
    entry = Map.get(items, hashed_key) |> Enum.find(fn x -> x.key == key end)
    {:reply, entry, state}
  end

  def handle_call({:delete, key}, _from, %{items: items, cap: cap} = state) do
    hashed_key = hash_key(key, cap)

    new_items =
      Map.update!(items, hashed_key, fn elements ->
        Enum.filter(elements, fn el -> el.key != key end)
      end)

    {:reply, :ok, %{state | items: new_items}}
  end

  def handle_cast({:put, key, value}, %{items: items, cap: cap, len: len} = state) do
    hashed_key = hash_key(key, cap)
    item = KVStore.StoredItem.new(key, value)

    new_state =
      case Map.fetch(items, hashed_key) do
        :error -> %{state | len: len + 1, items: Map.put(items, hashed_key, [item])}
        {:ok, entry} -> %{state | len: len + 1, items: Map.put(items, hashed_key, [item | entry])}
      end

    IO.inspect(new_state)

    new_state =
      if len == cap do
        rehash_keys(new_state)
      else
        new_state
      end

    {:noreply, new_state}
  end

  defp hash_key(key, cap) do
    key
    |> String.to_charlist()
    |> Enum.reduce(0, fn code, acc ->
      acc + code
    end)
    |> rem(cap)
  end

  defp rehash_keys(%{items: items, cap: cap, len: len}) do
    new_state = %{items: %{}, cap: cap + 15, len: len}

    IO.inspect Map.values(items)

    Enum.each(Map.values(items), fn elements->
      Enum.each(elements, fn el ->
        hashed_key = hash_key(el.key, new_state.cap)

        case Map.fetch(new_state.items, hashed_key) do
          :error -> %{new_state | items: Map.put(new_state.items, hashed_key, [el])}
          {:ok, entry} -> %{new_state| items: Map.put(new_state.items, hashed_key, [el | entry])}
        end
      end)
    end)

    new_state
  end
end
