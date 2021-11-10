# tentativa de criação de uma regressão linear, técnica matemática usada em modelos de machine learning
# Regressão linear é o processo de traçar uma reta através dos dados em um diagrama de dispersão.
# A reta resume esses dados, o que é útil quando fazemos previsões.
import matplotlib.pyplot as plt


class RegressaoLiner:
    """
    Calcula, com base em dois vetores passados,
    a previsão de determinado evento ocorrer
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.resultado = tuple()

    def regressao_linear(self):
        """
        recebe os dois vetores iniciais, x e y
        calcula os coeficientes da equação y = B + mA
        :return:
        """
        if len(self.x) >= 2 and len(self.y) >= 2:
            # calculo sistema linear:
            alpha = (self.y[1] - self.y[0]) / (self.x[1] - self.x[0])
            betha = self.y[1] - (alpha * self.x[1])
            self.resultado = (True, alpha, betha)
        else:
            raise Exception("\nSyntax Incorreta, você deve coletar mais dados\nCada vetor deve conter, no mínimo, "
                            "2 itens\n")

    def previsao_simples(self, ponto_valor):
        """
        recebe lista com 1 valor para previsão simples, poucos dados
        faz a estimativa da previsão
        :return:
        """
        if self.resultado:
            a = self.resultado[1]
            b = self.resultado[2]

            # cálculo
            y = (a * ponto_valor) + b
            return y

    def parametro(self):
        """
        faz uma média especial que serve de parametro para o aumento do grau de precisao
        :return:
        """
        media_x = sum(self.x) / len(self.x)
        media_y = sum(self.y) / len(self.y)
        media_total = (media_y + media_x) / 2
        return media_total

    def analise_grafica(self):
        """
        permite a visualização gráfica
        :return:
        """
        plt.figure()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Eventos e previsão aproximada")
        plt.plot(self.x, self.y, 'k.')
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    classe = RegressaoLiner([7, 10, 15, 30, 45, 60, 90, 102, 123], [8, 11, 16, 38.5, 52, 66, 78, 90, 122])
    classe.regressao_linear()
    print(f"A média do gráfico está por volta de {classe.parametro()}, logo, previsões próximas a esse valor, serão mais precisas")
    print(classe.previsao_simples(50))
    classe.analise_grafica()
