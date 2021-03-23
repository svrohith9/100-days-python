with open(
        ".\\100-days-python\\Day24\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names_list:
    names = names_list.readlines()

f = open
with open(
        ".\\100-days-python\\Day24\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as mail_body:
    mail_content = mail_body.read()
    for name in names:
        # strip() removes any extra spaces at the prefix and suffix
        new_mail = mail_content.replace("[name]", name.strip())
        with open(f".\\100-days-python\\Day24\\Mail Merge Project Start\\Output\\mail_to_{name.strip()}", mode="w") as completed_mail:
            completed_mail.write(new_mail)
