from abc import ABC, abstractclassmethod,abstractproperty
class Cliente:
    def __int__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_trans(self, conta, transacao):
        transacao.registrar(conta)
    def adcionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __int__(self, nome, data_nasc, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf

class Conta:
    def __int__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Saldo Insuficiente!!')

        elif valor > 0:
            self._saldo -= valor
            print('Operação realizada com sucesso!!')
            return True
        else:
            print('Operção falhou. Digite um valor válido!!')
        return False

    def depositar(self, valor):
        if valor > 0 :
            self._saldo += valor
            print('Depósito Realizado com sucesso!!')

        else:
            print('O valor informado é inválido!!')
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3 ):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque
        if excedeu_limite:
            print('Valor acima do permitido.Tente Novamente!!')

        elif excedeu_saques:
            print('Você execedeu o numero de saques permitidos por dia!!')
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f'''\
            Agência:>\t{self.agencia}
            C\C: \t\t{self.numero}
            Titular:\t{self.cliente.nome}
        '''

class Historico:
    def __int__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adc_transacoes(self, transacao):
        self._transacoes.append(
            {
                'Tipo': transacao.__class__.__name__,
                'Valor': transacao.valor,
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adc_transacoes(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adc_transacoes(self)
