programa {
	funcao inicio() {
	//	Fa�a um programa que receba um valor de uma compra e a
//quantidade de presta��es e mostre o valor das presta��es.

    real valor_compra,quant_prestacao,valor_pagar
    
    
    escreva("Digite o valor da sua compra:")
    leia(valor_compra)
    
    escreva("Quantas vezes deseja parcelar sua compras:")
    leia(quant_prestacao)
    
     
     valor_pagar=valor_compra/quant_prestacao
     
     escreva("O valor que vai pagar nas presta��o e de:",valor_pagar)
    


	}
}
