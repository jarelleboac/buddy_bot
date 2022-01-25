import round_robin
import send_emails

try:
    pairs = round_robin.main()

    send_emails.main(pairs)
except ValueError:
    print("Invalid action")

