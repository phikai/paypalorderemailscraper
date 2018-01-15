import quopri
import sys

with open('mbox.mbox') as fp:
	emailBuffer = []

	for line in fp:
		if (line.startswith("To: Karla Armstrong <petitechalet.etsy@gmail.com>")):
			emailStr = quopri.decodestring("".join(emailBuffer))

			strPos = emailStr.find("From:")
			if (strPos > -1):
				newLinePos = emailStr.find("\n", strPos)
				customerName = emailStr[strPos + 6:newLinePos]
				customerNames = customerName.split()
				if 0 <= 0 < len(customerNames):
					customerFName = customerNames[0]
					sys.stdout.write(customerFName.strip())
					sys.stdout.write(",")
				if 0 <= 1 < len(customerNames):
					customerLName = customerNames[1]
					sys.stdout.write(customerLName.strip())
					sys.stdout.write(",")

			strPos = emailStr.find("Reply-To:")
			if (strPos > -1):
				newLinePos = emailStr.find("\n", strPos)
				emailAddress = emailStr[strPos + 10:newLinePos].split("<")
				if 0 <= 0 < len(emailAddress):
					emailFinal = emailAddress[-1]
					sys.stdout.write(emailFinal.strip())
					sys.stdout.write(",")

			emailBuffer = []
		else:
			emailBuffer.append(line)
