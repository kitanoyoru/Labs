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
    {:ok, %{}}
  end

  def handle_call({:get, key}, _from, state) do
    hashed_key = hash_key(key)
    {:reply, Map.get(state, hashed_key), state}
  end

  def handle_call({:list}, _from, state) do
    {:reply, state, state}
  end

  def handle_cast({:put, key, value}, state) do
    hashed_key = hash_key(key)
    item = KVStore.StoredItem.new(key, value)
    {:noreply, Map.put(state, hashed_key, item)}
  end

  def handle_call({:delete, key}, state) do
    hashed_key = hash_key(key)
    {value, new_state} = Map.pop(state, hashed_key)
    {:reply, value, new_state}
  end

  def hash_key(key) do
    :crypto.hash(:md5, key) |> Base.encode16()
  end
end
