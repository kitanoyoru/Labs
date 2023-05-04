


pub trait IMemory {
    fn insert(&mut self, value: i32);
    fn in_range(start: &u32, end: &u32) -> Vec<Vec<i32>>; 
    fn sort(&mut self, direction: bool);
}

#[derive(Default, Debug, Clone)]
pub struct Memory {
    values: Vec<Vec<i32>>
} 

impl Memory {
    pub fn new(initial_values: Vec<Vec<i32>>) -> Self {
        Self {
            values: initial_values,
        }
    }
}

impl IMemory for Memory {
    fn insert(&mut self, value: i32) {
        self.values.push(ToBinary(value))
    }


    fn sort(&mut self) {
        self.values.iter_mut().for_each(|x| x.sort());
        self.values.sort_by_key(|x| x[0]);
    }

    fn in_range(start: &u32, end: &u32) -> Vec<Vec<i32>> {
    }
}

