package br.com.value.projects.dominio;

public class Resultado {

	private Participante participante;
	private double metrica;
	
	public Resultado(Participante participante, double metrica, int n) {
		this.participante = participante;
		this.metrica = metrica;
	}

	public Participante getParticipante() {
		return participante;
	}

	public double getMetrica() {
		return metrica;
	}
	
	
	
}
