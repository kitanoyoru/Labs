defmodule KVStore.StoredItem do
  use TypedStruct

  typedstruct enforce: true do
    field :key, String.t()
    field :value, String.t()
  end

  def new(key, value) do
    %KVStore.StoredItem{key: key, value: value}
  end
end
