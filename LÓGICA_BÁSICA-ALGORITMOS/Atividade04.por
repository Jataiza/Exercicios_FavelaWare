programa {
	funcao inicio() {
		//Fa�a um programa que leia o nome de um vendedor, o seu sal�rio e o total de vendas efetuadas. Sabe-se que o vendedor recebe 15% de 
		//comiss�o sobre as vendas efetuadas. 
		//Calcule a comiss�o emostre na tela: o nome do vendedor, o total de vendas, acomiss�o, o sal�rio fixo e o valor total do sal�rio.
		//F�rmula:(valor*15)/100 ou valor*0.15

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
        
        escreva("O nome do vendedor �:",nomevend)
        escreva("O salario do vendedor �:",salario)
        escreva("O salario do vendedor com comiss�o �:",salfinal)



















	}
	
	
	
}
