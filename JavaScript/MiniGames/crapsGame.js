// Objetivo: O jogador lança dois dados e tenta ganhar baseado em regras específicas.
// Regras:

// Ganhar: Se a primeira jogada resulta em 7 ou 11, o jogador ganha imediatamente (natural).
// Perder: Se a primeira jogada resulta em 2, 3 ou 12, o jogador perde (craps).
// Estabelecer um Ponto: Se a primeira jogada resulta em 4, 5, 6, 8, 9 ou 10, esse número se torna o "ponto".
// O jogador continua lançando até tirar o mesmo ponto novamente (ganha) ou um 7 (perde).

function lancarDados() {
    return Math.floor(Math.random() * 6) + 1 + Math.floor(Math.random() * 6) + 1;
}

function jogoDeCraps() {
    console.log("Bem-vindo ao jogo de Craps!");

    let primeiraJogada = lancarDados();
    console.log(`Sua primeira jogada é: ${primeiraJogada}`);

    if (primeiraJogada === 7 || primeiraJogada === 11) {
        console.log("Você fez um 'natural'. Você ganhou!");
    } else if (primeiraJogada === 2 || primeiraJogada === 3 || primeiraJogada === 12) {
        console.log("Você fez 'craps'. Você perdeu!");
    } else {
        let ponto = primeiraJogada;
        console.log(`Você fez um ponto: ${ponto}. Continue jogando para tentar tirar o mesmo número novamente.`);

        while (true) {
            let jogada = lancarDados();
            console.log(`Sua jogada é: ${jogada}`);

            if (jogada === ponto) {
                console.log("Você tirou seu ponto novamente. Você ganhou!");
                break;
            } else if (jogada === 7) {
                console.log("Você tirou 7. Você perdeu!");
                break;
            }
        }
    }
}

jogoDeCraps();


// MiniGame somente no Backend