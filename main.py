import os, time, msvcrt, sys
import validators
import keyboard
from app.git import Git

def main(text="Welcome to your EasyGit"):
    """
    Main function to display menu options and execute corresponding actions.

    Args:
        text (str, optional): Additional text to display. Defaults to "Welcome to your EasyGit".
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    Git.info()
    print()
    if text != "":
        print(text)
        print()
    print("[1] Clone")
    print("[2] Pull")
    print("[3] Push")
    print("[4] Add And Commit")
    print("[0] Exit")
    print()

if __name__ == "__main__":
    from app.explorer import Explorer
    main()
    while True:
        choice = msvcrt.getch()

        if choice == b'1':
            url = input("Enter remote repository URL : ")
            if not validators.url(url):
                main("Invalid remote repository URL")
            else:
                Git.clone(url)
        elif choice == b'2':
            Git.pull()
        elif choice == b'3':
            print("Enter your commit (press Enter to confirm):")
            text = input().strip()
            if text == '0':
                main()
                continue
            elif text == "" or text is None:
                text = "Automated easygit commit"
            else:
                text = text + " - easygit"
            Git.run(text)
        elif choice == b'4':
            # print("Similar to git commit -am")
            msg = input("Enter commit message: ")
            if msg == "" or msg is None:
                print("Message cannot be empty")
            else:
                Git.addcommit(msg)

        elif keyboard.is_pressed('enter'):
            Explorer.vscode()
            pass
        elif choice == b' ':  # Space key
            main()
        elif choice == b'M':  # Right arrow key
            Explorer.next()
        elif choice == b'K':  # Left arrow key
            Explorer.back()

        elif choice == b'0':
            print("Exiting...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Invalid choice. Please try again.")