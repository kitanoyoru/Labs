from lab7.memory import Memory


if __name__ == "__main__":
    values = [10, 12, 36, 72, 15, 64, 255]
    m = Memory(values)
    
    template = 23
    print(f"Seach by template {template}:", m.search_by_template(template))

    bool_func = "a&b&c&d&e&f&g&h"
    print(f"Check by bool func {bool_func}:", m.check_by_bool_func(bool_func))

