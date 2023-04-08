defmodule HashTable do
  use GenServer

  @spec start(any) :: :ignore | {:error, any} | {:ok, pid}
  def start(args) do
    GenServer.start(__MODULE__, args, name: :hashtable)
  end

  @spec get(atom | pid | {atom, any} | {:via, atom, any}, any) :: any
  def get(sid, key) do
    GenServer.call(sid, {:get_item, key})
  end

  @spec put(atom | pid | {atom, any} | {:via, atom, any}, any, any) :: :ok
  def put(sid, key, value) do
    GenServer.cast(sid, {:put_item, key, value})
  end

  @spec delete(atom | pid | {atom, any} | {:via, atom, any}, any) :: :ok
  def delete(sid, key) do
    GenServer.cast(sid, key)
  end

  @spec init :: {:ok, %{}}
  def init do
    state = %{}
    {:ok, state}
  end

  @spec handle_cast({:put_item, any, any}, any, map) :: {:reply, :ok, map}
  def handle_cast({:put_item, key, value} , _from, state) do
    state = Map.put(state, key, value)
    {:reply, :ok, state}
  end

  def handle_cast({:delete_item, key}, _from, state) do
    state = Map.delete(state, key)
    {:reply, :ok, state}
  end

  def handle_call({:get_item, key}, _from ,state) do
    item_or_none = Map.fetch(state, key)
    case item_or_none do
      {:ok, value} -> {:reply, {:ok, value}, state}
      :error -> {:reply, :error, state}
    end
  end


  defp hash_key(key) do
    :ok
  end
end
