// Identity as exclusive possession: affine types in Rust.
// Run: rustc rust_linear_identity.rs -o /tmp/rli && /tmp/rli

fn consume(s: String) -> usize { s.len() }

fn main() {
    // A String owns heap memory: it is a THING, not a fact.
    let x = String::from("unclonable by default");

    // Moving it invalidates the source -- contraction is denied:
    let y = x;
    // println!("{}", x);   // <-- uncomment: ERROR, "value borrowed after move"
    // Girard's linear logic, as a compiler diagnostic.

    // Borrowing = temporary, non-consuming access (no ownership transfer):
    let n = y.len();               // &self borrow, y still ours
    println!("borrowed length: {}", n);

    // By-value call = the linear arrow A ⊸ B: the argument is CONSUMED.
    let m = consume(y);
    // println!("{}", y);   // <-- uncomment: ERROR, y was consumed
    println!("consumed, got: {}", m);

    // The exponential !A -- copyability restored, but MARKED and PAID FOR:
    use std::rc::Rc;
    let shared = Rc::new(String::from("copyable, visibly"));
    let s2 = Rc::clone(&shared);   // duplication is explicit and counted
    println!("refcount now: {}", Rc::strong_count(&shared));
    drop(s2);

    // Quantum computing forbids cloning unknown states (no-cloning theorem);
    // Rust forbids cloning owned memory implicitly. Two fields, one insight:
    // having a thing does not mean having it twice.
}
