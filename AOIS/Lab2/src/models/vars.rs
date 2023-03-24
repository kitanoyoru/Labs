use indexmap::map::IndexMap;

pub struct VarValues(IndexMap<String, bool>);

impl VarValues {
    pub fn new(names: &[String]) -> Self {
        let mut hm = IndexMap::<String, bool>::new();

        for name in names.iter().map(Clone::clone) {
            hm.entry(name).or_insert(true);
        }

        VarValues(hm)
    }

    pub fn get_value<T: ToString>(&self, name: T) -> bool {
        *self.0.get(&name.to_string()).unwrap()
    }

    pub fn names(&self) -> impl Iterator<Item = &String> {
        self.0.keys()
    }

    pub fn values(&self) -> Vec<bool> {
        self.0.values().copied().collect()
    }

    pub fn advance(&mut self) -> bool {
        self.0.values_mut().rev().any(|value| {
            *value = !*value;
            !*value
        })
    }
}
