defmodule Lab6 do
  use Application

  def start(_type, _args) do
    KVStore.Supervisor.start_link(name: KVStore.Supervisor)
  end
end
