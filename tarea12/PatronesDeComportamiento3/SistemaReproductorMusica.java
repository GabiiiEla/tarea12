public class SistemaReproductorMusica {

    public static void main(String[] args) {
        System.out.println("--- Usando el Reproductor de Música directamente (MP3) ---");
        ReproductorMusica miReproductor = new ReproductorMusica() {
            @Override
            public void reproducirMp3(String nombreArchivo) {
                System.out.println("Reproduciendo archivo MP3: " + nombreArchivo);
            }
        };
        miReproductor.reproducirMp3("cancion_favorita.mp3");
        System.out.println("\n--- Usando el Reproductor WAV a través del Adaptador ---");
    
        ReproductorWAV reproductorWAVExistente = new ReproductorWAV();
        ReproductorMusica adaptadorWAV = new AdaptadorReproductorWAV(reproductorWAVExistente);
        adaptadorWAV.reproducirMp3("otra_cancion.mp3"); 
        System.out.println("\n--- Demostración de incompatibilidad directa (si no usáramos el adaptador) ---");
        
    }
}