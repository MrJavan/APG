# README

## Password Generator Script

This Python script generates secure passwords based on the user's preferred level of security. The generated passwords can include uppercase letters, lowercase letters, numbers, and special characters. The password is also automatically copied to the clipboard using the **`pyperclip`** library.

---

### Features:
1. **Secure Password:**  
   Includes uppercase and lowercase letters.  
2. **Secure Plus Password:**  
   Includes letters and numbers.  
3. **Ultra Secure Password:**  
   Includes letters, numbers, and special characters.

---

### Usage:

1. **Run the script:**
   ```bash
   python main.py


2. **Choose Password Security Level:**
You will be prompted to select a level of security:

- **[1] Secure Password:** Letters only.  
- **[2] Secure Plus Password:** Letters and numbers.  
- **[3] Ultra Secure Password:** Letters, numbers, and characters.

---

3. **Specify Password Length:**
Enter a number greater than or equal to **10**.  
If the input is invalid, the script will prompt you to try again.

---

4. **Password Generation:**
The generated password will be displayed and automatically copied to your clipboard.


### Requirements:
- **Python 3.x**  

#### Libraries:
- `pyperclip`  
- `os`  
- `random`  

To install **pyperclip**, use the following command:
```bash
pip install pyperclip
