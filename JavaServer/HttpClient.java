package JavaServer;

import java.io.*;
import java.net.*;

public class HttpClient {
    public static void main(String[] args) {
        // Verificar que se pasaron los argumentos necesarios
        if (args.length < 3) {
            System.out.println("Uso: java HttpClient <serverIP> <port> <imagePath>");
            return;
        }

        // Obtener los parámetros desde la línea de comandos
        String serverIP = args[0];
        int port = Integer.parseInt(args[1]);
        String imagePath = args[2];

        File fileToSend = new File(imagePath);

        if (fileToSend.exists()) {
            try (FileInputStream inputS = new FileInputStream(fileToSend);
                 Socket socket = new Socket(serverIP, port);
                 DataOutputStream outputS = new DataOutputStream(socket.getOutputStream())) {

                String fileName = "image.jpg";
                byte[] fileNameBytes = fileName.getBytes();

                byte[] fileContentBytes = new byte[(int) fileToSend.length()];
                inputS.read(fileContentBytes);

                outputS.writeInt(fileNameBytes.length);
                outputS.write(fileNameBytes);

                outputS.writeInt(fileContentBytes.length);
                outputS.write(fileContentBytes);

                System.out.println("ARCHIVO ENVIADO: " + fileName);

            } catch (IOException e) {
                System.out.println("Error al enviar el archivo: " + e.getMessage());
            }
        } else {
            System.out.println("El archivo no existe: " + imagePath);
        }
    }
}
