// OBJETIVO: O jogador deve apostar em um número e ganhar se esse número aparecer entre os dados lançados. Caso contrário, ele perde. bem simples.

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function lancarDados() {
    return Math.floor(Math.random() * 6) + 1;
}

function chuckALuck() {
    console.log("Bem-vindo ao Chuck-a-Luck!");

    rl.question("Escolha um número entre 1 e 6 para apostar: ", (input) => {
        const aposta = parseInt(input, 10);

        if (aposta < 1 || aposta > 6 || isNaN(aposta)) {
            console.log("Número inválido! Escolha um número entre 1 e 6.");
            rl.close();
            return;
        }

        const dados = [lancarDados(), lancarDados(), lancarDados()];
        console.log(`Os dados foram lançados: ${dados.join(", ")}`);

        const contagem = dados.filter(dado => dado === aposta).length;

        if (contagem > 0) {
            console.log(`Você ganhou! O número ${aposta} apareceu ${contagem} vez(es).`);
        } else {
            console.log(`Você perdeu! O número ${aposta} não apareceu.`);
        }

        rl.close();
    });
}
chuckALuck();