interface ReproductorMusica {
    void reproducirMp3(String nombreArchivo);
}

class ReproductorWAV {
    public void reproducir(String archivoWav) {
        System.out.println("Reproduciendo archivo WAV: " + archivoWav);
    }
}

class AdaptadorReproductorWAV implements ReproductorMusica {
    private ReproductorWAV reproductorWAV;

    public AdaptadorReproductorWAV(ReproductorWAV reproductorWAV) {
        this.reproductorWAV = reproductorWAV;
    }

    @Override
    public void reproducirMp3(String nombreArchivo) {
        System.out.println("ADAPTADOR: Convirtiendo MP3 a WAV y enviando al reproductor WAV...");
        reproductorWAV.reproducir(nombreArchivo.replace(".mp3", ".wav"));
    }
}
