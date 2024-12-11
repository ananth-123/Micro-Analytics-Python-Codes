def check_password(password: str) -> tuple[list, list, str]:
    rules = {
        "length": {
            "rule": len(password) >= 8,
            "fail_message": "Password must be at least 8 characters long",
            "pass_message": "✓ Length requirement met (8+ characters)"
        },
        "uppercase": {
            "rule": any(char.isupper() for char in password),
            "fail_message": "Password must contain at least one uppercase letter",
            "pass_message": "✓ Contains uppercase letter"
        },
        "lowercase": {
            "rule": any(char.islower() for char in password),
            "fail_message": "Password must contain at least one lowercase letter",
            "pass_message": "✓ Contains lowercase letter"
        },
        "digit": {
            "rule": any(char.isdigit() for char in password),
            "fail_message": "Password must contain at least one number",
            "pass_message": "✓ Contains number"
        },
        "special_char": {
            "rule": any(not char.isalnum() for char in password),
            "fail_message": "Password must contain at least one special character",
            "pass_message": "✓ Contains special character"
        },
        "no_spaces": {
            "rule": " " not in password,
            "fail_message": "Password cannot contain spaces",
            "pass_message": "✓ No spaces found"
        }
    }
    
    passed = []
    failed = []
    feedback = []
    
    for rule_name, rule_data in rules.items():
        if rule_data["rule"]:
            passed.append(rule_name)
            feedback.append(rule_data["pass_message"])
        else:
            failed.append(rule_name)
            feedback.append("✗ " + rule_data["fail_message"])
    
    summary = "\nPassword Rules Check:\n"
    summary += "\n".join(feedback)
    
    summary += f"\n✓ Passed: {len(passed)} rules"
    if passed:
        summary += f" ({', '.join(passed)})"
    summary += f"\n✗ Failed: {len(failed)} rules"
    if failed:
        summary += f" ({', '.join(failed)})"
        
    if len(passed) == 6:
        summary += "\n\nSUCCESS: Password meets all requirements!"
    else:
        summary += "\n\nFAILED: Please fix the failed rules and try again."
    
    return passed, failed, summary

def get_password_input() -> str:
    while True:
        try:

            password = input("\nEnter your password: ").strip()
            
            if password.lower() == 'quit':
                return 'quit'
            
            if not password:
                print("Password cannot be empty. Please try again.")
                continue
                
            if len(password) > 50: 
                print("⚠️  Password is too long. Please keep it under 100 characters.")
                continue
                
            return password
            
        except Exception as e:
            print(f"\n An error occurred: {e}")
            print("Please try again.")
            continue

def main():
    print("Password Checker:")
    print("=" * 40)
    print("• Type your password to check its strength")
    print("• Press Ctrl+C or type 'quit' to exit")
    print("=" * 40)
    
    while True:
        password = get_password_input()
        
        if password == 'quit':
            print("\nProgram terminated.")
            break
            
        passed, failed, feedback = check_password(password)
        print(feedback)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}")
        print("Program terminated.")
