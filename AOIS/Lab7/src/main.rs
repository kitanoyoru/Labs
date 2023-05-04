use memory::Memory;

fn main() {
    let initial_values = vec![255,6212,2341,23421,7593,20,1234,8139,50000,1];
    let mem = Memory(initial_values);
    mem.result()
}