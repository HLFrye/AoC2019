use std::fs::File;
use std::io::{BufRead, BufReader};

fn calculate_fuel(weight: i64) -> i64 {
  let fuel_weight = (weight/3) - 2;
  if fuel_weight <= 0 {
    return 0;
  }
  return fuel_weight + calculate_fuel(fuel_weight);
}

fn main() {
    let f = File::open("input.txt").unwrap();
    let f = BufReader::new(f);

    let total = f.lines()
      .map(|line| line
        .expect("Unable to read line")
        .parse::<i64>()
        .expect("Unable to parse line"))
      .map(calculate_fuel)
      .sum::<i64>();

    println!("{}", total);
}
