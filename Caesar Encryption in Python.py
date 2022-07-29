"""Caesar Encryption in Python
simple Encryption in Python 
Example:
To begin encrypting, write your message in English on a piece of paper. For this example, we’ll encrypt the message THE SECRET PASSWORD IS ROSEBUD. Next, spin the inner wheel of the cipher wheel until its slots match up with slots in the outer wheel. Notice the dot next to the letter A in the outer wheel. Take note of the number in the inner wheel next to this dot. This is the encryption key.
For example, in Figure 1-1, the outer circle’s A is over the inner circle’s number 8. We’ll use this encryption key to encrypt the message in our example, as shown in Figure 1-2.
After you encrypt the entire message, the original message, THE SECRET PASSWORD IS ROSEBUD, becomes BPM AMKZMB XIAAEWZL QA ZWAMJCL. Notice that non-letter characters, such as the spaces, are not changed"""
import string
def Caesar(text,shift,alps):
    def shift_alp(alp):
        return alp[shift:]+alp[:shift]
    shif_done=tuple(map(shift_alp,alps))
    final_alp=''.join(alps)
    final_shift_alp=''.join(shif_done)
    t_map=str.maketrans(final_alp,final_shift_alp)
    return text.translate(t_map)
text_input=input()
print(Caesar(text_input,8,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))
