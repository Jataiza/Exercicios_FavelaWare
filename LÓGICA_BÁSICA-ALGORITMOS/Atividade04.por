programa {
	funcao inicio() {
		//Faça um programa que leia o nome de um vendedor, o seu salário e o total de vendas efetuadas. Sabe-se que o vendedor recebe 15% de 
		//comissão sobre as vendas efetuadas. 
		//Calcule a comissão emostre na tela: o nome do vendedor, o total de vendas, acomissão, o salário fixo e o valor total do salário.
		//Fórmula:(valor*15)/100 ou valor*0.15

        cadeia nomevend
        real salario,total_vend,comissao,salfinal
        
        escreva("Digite o nome do vendendor:")
        leia(nomevend)

        escreva("Digite o salario do vendendor:")
        leia(salario)

        escreva("Digite o total de vendas do vendendor")
        leia(total_vend)
        
        comissao =salario*0.15
        salfinal=salario+comissao
        
        escreva("O nome do vendedor é:",nomevend)
        escreva("O salario do vendedor é:",salario)
        escreva("O salario do vendedor com comissão é:",salfinal)



















	}
	
	
	
}
