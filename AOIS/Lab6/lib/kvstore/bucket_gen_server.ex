defmodule KVStore.BucketGenServer do
  use GenServer

  # Public interface

  def start_link(options \\ []) do
    GenServer.start_link(__MODULE__, :ok, options)
  end

  def load_json(bucket) do
    GenServer.cast(bucket, {:load_json})
  end

  def get(bucket, key) do
    GenServer.call(bucket, {:get, key})
  end

  def list(bucket) do
    GenServer.call(bucket, {:list})
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
    {:ok, %{size: 0, capacity: 5 items: {}}
  end

  def handle_call({:list}, _from, %{items: items} = state) do
    {:reply, items, state}
  end

  def handle_call({:get, key}, _from, %{items: items} = state) do
    hashed_key = hash_key(key)
    entry = Map.get(items, hashed_key) |> Enum.find(fn x -> x.key == key end)
    {:reply, entry, state}
  end

  def handle_call({:delete, key}, _from, %{size: size, items: items} = items) do
    hashed_key = hash_key(key)

    new_state = Map.update!(state, hashed_key, fn items ->
      Enum.filter(items, fn item -> item.key != key end)
    end)

    IO.inspect new_state


    {:reply, :ok, new_state}
  end

  def handle_cast({:load_json}, state) do
    filename = Application.fetch_env!(:my_app, :data_path)
    #filename = "/Users/kitanoyoru/Labs/AOIS/Lab6/data/data.json"
    {:ok, data} = read_data_json(filename)

    Enum.each(data, fn {key, value} ->
      hashed_key = hash_key(key)
      item = KVStore.StoredItem.new(key, value)

      case Map.fetch(state, hashed_key) do
        :error -> state = Map.put(state, hashed_key, [item])
        {:ok, entry} -> state = Map.put(state, hashed_key, [item | entry])
      end
    end)

    {:noreply, state}
  end

  def handle_cast({:put, key, value}, state) do
    hashed_key = hash_key(key)
    item = KVStore.StoredItem.new(key, value)

    case Map.fetch(state, hashed_key) do
      :error -> {:noreply, Map.put(state, hashed_key, [item])}
      {:ok, entry} -> {:noreply, Map.put(state, hashed_key, [item | entry])}
    end
  end

  defp hash_key(key) do
    #:crypto.hash(:md5, key) |> Base.encode16()
    String.length(key)
  end

  defp read_data_json(filename) do
    with {:ok, body} <- File.read(filename),
         {:ok, json} <- Poison.decode(body), do: {:ok, json}
  end
end
