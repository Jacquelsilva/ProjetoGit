# TaskFlow API

# 🚀 Projeto Flask com CI/CD - Integração e Entrega Contínua

Projeto desenvolvido na disciplina de Integração e Entrega Contínua (DSM – 4º semestre), aplicando práticas modernas de versionamento, integração contínua e fluxo profissional de desenvolvimento.

🎯 Objetivo  
Aplicar na prática: versionamento com Git, uso de branches, Pull Requests, integração contínua (CI) com GitHub Actions, testes automatizados com Pytest, proteção da branch principal e simulação de deploy.

🧱 Estrutura do Projeto  
taskflow-api/  
├── src/  
│   └── app.py  
├── tests/  
│   └── test_app.py  
├── requirements.txt  
└── .github/  
    └── workflows/  
        └── ci.yml  

🌐 Rotas da API  
/ → Página inicial  
/status → Status da API  
/sobre → Informações do projeto  
/livros → Lista de livros  
/autores → Lista de autores  
/contato → Página de contato  
/cadastro-livro → Cadastro de livros  

🧪 Testes Automatizados  
Utilizado Pytest para validar o funcionamento da aplicação.  
Os testes verificam o status das rotas garantindo que a API está respondendo corretamente.  

🔄 Fluxo de Desenvolvimento  
criar branch → desenvolver funcionalidade → commit → push → Pull Request → CI executa automaticamente → (sucesso) merge permitido → (falha) merge bloqueado  

⚙️ Integração Contínua (CI)  
Pipeline configurada com GitHub Actions com as seguintes etapas:  
- Clone do repositório  
- Configuração do Python  
- Instalação de dependências  
- Execução dos testes com pytest  
- Validação automática a cada push e Pull Request  

🧪 Simulação de Falhas  
Durante o projeto foram simulados diversos erros para validação da CI:  
- erro de sintaxe  
- dependência inválida  
- erro em testes  
- arquivo inexistente  

Todos os erros foram identificados automaticamente pela pipeline e corrigidos com base nos logs gerados.

🔒 Proteção da Branch  
A branch main foi protegida com:  
- Pull Request obrigatório  
- CI obrigatória para merge  
- Bloqueio automático de merge quando há erro  

🚀 Deploy Simulado  
Foi adicionada uma etapa final na pipeline para simular o processo de deploy:  

- name: Simular Deploy  
  run: echo "Deploy realizado com sucesso"  

📊 Resultado Final  
CI funcionando  
Testes automatizados  
Pull Requests obrigatórios  
Merge controlado  
Pipeline validando automaticamente  
Deploy simulado executado  

💡 Aprendizados  
Uso profissional do Git  
Fluxo real de desenvolvimento em equipe  
Integração contínua com validação automática  
Leitura e análise de erros em pipelines  
Organização e boas práticas de código  

🏁 Conclusão  
Este projeto representa a implementação completa de um fluxo moderno de desenvolvimento com CI/CD, simulando práticas utilizadas em ambientes profissionais.

👩‍💻 Desenvolvido por Jacqueline Leite Da Silva
