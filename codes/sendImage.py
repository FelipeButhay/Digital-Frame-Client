import subprocess

def sendImage(ip: str, proyect_direc: str) -> str:
    port = "8080"
    image_path = f"{proyect_direc}/Images/image.jpg"

    compilation = subprocess.run(["javac", "JavaServer/HttpClient.java"], capture_output=True, text=True)
    
    if compilation.returncode == 0:
        execution = subprocess.run(["java", "JavaServer/HttpClient", ip, str(port), image_path], capture_output=True, text=True)

        return execution.stdout
    else:
        return compilation.stderr
