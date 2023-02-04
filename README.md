# Ciphering Functions
### A little background information
So what do you do when your sibling walks into your room with a piece of paper which says "Don't talk to me until you
figure this out" followed by a cipher? Well you figure it out! Now I could clearly tell it looked like a shifted cipher
but I had no idea by how much. Instead of calculating each possibility individually, I wrote a little python function to
calculate the character shift, which ended up becoming a set of functions for me to practice writing in python.

Note: These are some pretty old functions uploaded for posterity

### Functions
They're pretty straight forward however there's comments on what they do specifically in the `Ciphering_Functions.py` file
- `print_all_shifts_to(phrase, no_of_shifts)`
- `shift_by(phrase, no_of_shifts)`
- `solve_emperors_shift(phrase)`
- `create_emperors_shift(phrase)`
- `create_rot1_shift(phrase)`
- `uasi_shift(phrase)`
- `qwerty_shift(phrase)`
- `inv_qwerty_shift(phrase)`
- `square_cipher(phrase)`
- `inv_square_cipher(phrase)`

Helper functions `next_vowel` and `next_letter` are also included in a separate `Helpers.py` file