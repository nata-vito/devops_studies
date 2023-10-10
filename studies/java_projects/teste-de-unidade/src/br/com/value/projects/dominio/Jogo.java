package br.com.value.projects.dominio;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Jogo {

	private String descricao;
	private List<Resultado> resultados;
	
	public Jogo(String descricao) {
		this.descricao = descricao;
		this.resultados = new ArrayList<Resultado>();
	}
	
	public void anota(Resultado resultado) {
		if(resultados.isEmpty() || 
                !resultados.get(ultimoResultadoVisto()).getParticipante().equals(resultado.getParticipante())) {
            resultados.add(resultado);
        }
		
		
	}

	public double calculaMedia(Jogo jogo) {
		
		double resTotal = 0.0;
		for (int i = 0; i < jogo.resultados.size() ; i++) {
			resTotal += jogo.resultados.get(i).getMetrica();
		}
		
		return resTotal / jogo.resultados.size();
	}

	private int ultimoResultadoVisto() {
		return resultados.size()-1;
	}

	public String getDescricao() {
		return descricao;
	}

	public List<Resultado> getResultados() {
		return Collections.unmodifiableList(resultados);
	}

	
	
}
