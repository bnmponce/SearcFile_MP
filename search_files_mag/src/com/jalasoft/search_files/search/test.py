import win32security
def get_owner(filename):
    file_and_folder = win32security.GetFileSecurity(filename, win32security.OWNER_SECURITY_INFORMATION)
    username = win32security.LookupAccountSid(None, file_and_folder.GetSecurityDescriptorOwner())
    return username[0]

print(get_owner("C:\\Users\HERMANOS\Downloads\Los Extermineitors 1 DVDRiP (Completa).mp4"))