import subprocess
def mergeRelease():
    try:
        subprocess.run(["git","checkout","main"])
        subprocess.run(["git","pull", "develop"])
        subprocess.run("git","merge","develop")
        
    except Exception as error:
        return f"Ett fel uppstod: {error}"
    
mergeRelease()
