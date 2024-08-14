# Vehicle Management System

Este é um sistema de gerenciamento de veículos desenvolvido em Python utilizando PyQt5 e MySQL. O sistema permite adicionar, buscar, listar, editar e deletar veículos no banco de dados.

## Funcionalidades

- **Adicionar Veículo**: Permite adicionar um novo veículo ao banco de dados.
- **Listar Todos os Veículos**: Exibe todos os veículos cadastrados em uma tabela.
- **Buscar Veículo**: Realiza a busca de veículos pelo ID, placa ou cor.
- **Editar Veículo**: Permite editar os detalhes de um veículo selecionado.
- **Deletar Veículo**: Remove um veículo do banco de dados.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Biblioteca GUI**: PyQt5
- **Banco de Dados**: MySQL

## Estrutura do Projeto

- `main.py`: Arquivo principal que inicializa a aplicação e define a interface do usuário.
- `dbConnection.py`: Contém a classe `DatabaseConnection`, responsável pela conexão e operações no banco de dados MySQL.
- `vehicle.py`: Define a classe `Vehicle`, que representa os atributos de um veículo.
- `EditVehicleDialog.py`: Implementa a janela de diálogo para editar os detalhes de um veículo.
- `style.py`: Aplica estilos personalizados à interface do usuário.
- `README.md`: Documento de descrição do projeto.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/tairony-cristian/vehicle-management-system.git

2. **Crie o banco de dados MySQL:**

    CREATE DATABASE vehicle_management;

3. **Crie a tabela de veículos:**

    USE vehicle_management;

    CREATE TABLE vehicles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        plate VARCHAR(255) NOT NULL,
        brand VARCHAR(255) NOT NULL,
        year INT NOT NULL,
        color VARCHAR(255) NOT NULL,
        renavam VARCHAR(255) NOT NULL
    );

4. **Instale as dependências:**

   pip install -r requirements.txt

**Como Executar**
    
Após a instalação, você pode executar a aplicação com o comando:
python main.py

 
 