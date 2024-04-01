class AlunoFatec:
    '''
    Descrição:
        Representa um aluno em um curso da Fatec.
    '''     
    
    def __init__(self, nome: str, semestre: int = 0, curso: str = None) -> None:
        """
        Inicializa um objeto AlunoFatec com o nome, semestre e curso fornecidos.
        
        Args:
            nome (str): O nome do aluno.
            semestre (int): O semestre atual do aluno (o padrão é 0).
            curso (str): O nome do curso em que o aluno está matriculado (o padrão é None).
        """
        self.nome = nome
        self.semestre = semestre
        self.curso = curso

    def exibir_informacoes_aluno(self) -> None:
        '''
        Exibe informações sobre o aluno.
        '''
        print(f'Aluno: {self.nome}, Semestre: {self.semestre}, Curso: {self.curso}')
        
class NotasAluno(AlunoFatec):
    
    def __init__(self, nome: str, semestre: int = 0, curso: str = None) -> None:
        """
        Inicializa um objeto NotasAluno representando as notas de um aluno da Fatec.
        
        Args:
            nome (str): O nome do aluno.
            semestre (int): O semestre atual do aluno (o padrão é 0).
            curso (str): O nome do curso em que o aluno está matriculado (o padrão é None).
        """
        super().__init__(nome, semestre, curso)
        self.notas = []
    
    def adicionar_nota(self, nota: float) -> None:
        """
        Adiciona uma nota ao registro do aluno.
        
        Args:
            nota (float): A nota a ser adicionada.
        """
        self.notas.append(nota)
        
    def exibir_notas(self) -> None:
        """
        Exibe as notas do aluno.
        """
        print(f'Notas: {self.notas}')


class GerenciadorMatriculas:
    def __init__(self) -> None:
        """
        Inicializa um objeto GerenciadorMatriculas responsável por gerenciar a matrícula de alunos.
        """
        print('''Selecione uma opção:
             [1] - Registrar Aluno 
             [2] - Adicionar Notas
             
             ''')
        escolha = int(input("Escolha: "))
        if escolha == 1:
            self.registrar_aluno()
    
    def registrar_aluno(self) -> None:
        """
        Registra um novo aluno.
        """
        nome = input('Digite o nome do aluno: ')
        curso = input('Digite o nome do curso: ')
        # Cria um novo objeto NotasAluno com semestre padrão
        aluno = NotasAluno(nome, curso=curso)
        aluno.exibir_informacoes_aluno()
        aluno.exibir_notas()

# Ponto de entrada do programa
GerenciadorMatriculas()
