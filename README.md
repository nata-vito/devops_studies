# DevOps Studies

Neste repositório, aplico alguns estudo sobre devops utilizando Python como linguagem principal. Utilizo as blibliotecas Pytest para realizar testes, a Covarege que extrair metricas sobre a cobertura dos meus testes em relação a aplicação e autoções com o GitActions para build do pacote e testes automatizados. Sinta-se livre para colaborar com o projeto!

---
### Pre-requisitos
- Anaconda 


### Instalação 
```
# Ative o ambiente
conda create --name <nome-ambiente> python=3.9
conda activate <nome-ambiente>

git clone https://github.com/nata-vito/devops_studies.git
cd devops_studies
pip install -r requirements.txt
```




## Utilização

```
cd ac1

# Executa os testes e cobertura de testes
coverage run --source=./ -m pytest -v tests

# Report no terminal
coverage report

# Report via HTML
coverage html
```

Para a cobertura do Covarege ficar em 100%, basta descomentar os testes fail, mas tenha em mente que a sua o build do GitHub Actions falhará.

## 🤝 Collaborators

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/64169072?v=4" width="100px;" alt="Foto do Natanael Vitorino no GitHub"/><br>
        <sub>
          <b>Natanael Vitorino</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---