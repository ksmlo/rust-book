fn main() {
    let price = 98000.0;
    let sender_a = 1200.0;
    let a_price = price * 0.8 - sender_a;
    let b_price = price * 0.9;

    println!("{}社の方が安い", if a_price > b_price { "B" } else { "A" });
}
