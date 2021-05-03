console.log(`Trabalhando com condicionais`);


const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio De Janeiro`
)

const idadeComprador = 10;
const estaAcompanhada = true;
console.log("Destinos possiveis: ");
console.log(listaDeDestinos);

if(idadeComprador >= 18 ){
    console.log("Comprador Maior de Idade")
    listaDeDestinos.splice(1, 1);//removendo item
}else if(estaAcompanhada == true){
        console.log("Comprador esta acompanhada")
    }else{
    console.log("Nao e maior de idade e nao vender")
    }


console.log(listaDeDestinos);

