programa
{
	
	funcao inicio()
	{
		real altura, peso, imc

		escreva("Insira a sua altura em metros:")
		leia(altura)
		escreva("Agora insira seu peso em kg:")
		leia(peso)

		imc=(peso/(altura*altura))

		se(imc<18.5){
			escreva("Você está abaixo do seu peso ideal")
		}
		senao se(imc>18.5 e imc<24.9){
			escreva("Você está na faixa de peso ideal")
		}
		senao se(imc>25 e imc<29.9){
			escreva("Você está acima do peso")
		}
		senao se(imc>30 e imc<40){
			escreva("Você está em estado de obesidade")
		}
		senao se(imc>40){
			escreva("Você está em estado de obesidade mórbida")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 0; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */