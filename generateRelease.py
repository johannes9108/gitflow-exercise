import subprocess

def loadCurrentVersionNumber():
    try:
        with open("versionNumber.txt", "r") as file:
            line = file.readline()
        return line
    except Exception as error:
        return f"Ett fel uppstod: {error}"
def generateRelease():
    try:
        currentVersion = loadCurrentVersionNumber()
        newVersion = incrementVersion(currentVersion)
        subprocess.run(["git", "checkout","-b",f"release-{newVersion}"])
        saveNewVersionToFile(newVersion)
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Release {newVersion}"])
        return newVersion
    except Exception as error:
        return f"Ett fel uppstod: {error}"
    
def saveNewVersionToFile(newVersion):
    try:
        with open("versionNumber.txt", "w") as file:
            file.write(newVersion)
    except Exception as error:
        return f"Ett fel uppstod: {error}"
def incrementVersion(version):
    version_list = [int(x) for x in version.split(".")]
    version = f"{version_list[0]+1}.{version_list[1]}.{version_list[2]}"
    return version
def pushRelease(version):
    try:
        subprocess.run(["git", "push", "origin", f"release-{version}"])
    except Exception as error:
        return f"Ett fel uppstod: {error}"

print("Kör ett release script")

newVersion = generateRelease()
pushRelease(newVersion)
# mergeRelease()