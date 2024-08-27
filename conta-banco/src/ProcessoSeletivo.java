import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class ProcessoSeletivo {
    public static void main(String[] args) {
        System.out.println("PROCESSO SELETIVO");
        String [] candidatos = {"FELIPE","MARIA","JULIA","PAULO","ARTUR"};
        for (String candidato : candidatos) {
            entrandoContato(candidato);
        }
    }

    static void entrandoContato (String candidato) {
        int tentativasRealizadas = 1;
        boolean continuarTentando = true, atendeu = false;
        do { 
            atendeu = atender();
            continuarTentando = !atendeu;
            if (continuarTentando)
                tentativasRealizadas++;
            else
                System.out.println("Contato realizado com sucesso.");
        } while (continuarTentando && tentativasRealizadas < 3);

        if (atendeu)
            System.out.println("Conseguimos contato com " + candidato + " na " + tentativasRealizadas + " tentiva");
        else   
            System.out.println("Não cosnseguimos contato com " + candidato + ".");
    }
    
    static boolean atender () {
        return new Random().nextInt(3) == 1;
    }
    
    static void exibirirSelecionados () {
        String [] candidatos = {"FELIPE","MARIA","JULIA","PAULO","ARTUR"};
        for (String candidato : candidatos)
            System.out.println("O candidato selecionado foi " + candidato);
    }

    static void selecaoCandidatos () {
        String [] candidatos = {"FELIPE","MARIA","JULIA","PAULO","ARTUR","MELISSA","FABRICIO","BIANCA"};
        int candidatosSelecionados = 0, candidatosAtual = 0;
        
        while (candidatosSelecionados < 5 && candidatosAtual < candidatos.length) {
            String candidato = candidatos[candidatosAtual];
            double salarioPretendido = valorPretendido();
            System.out.println("O candidato " + candidato + " solicitou este valor de salario: " + salarioPretendido);
            if (salarioPretendido <= 2000) {
                System.out.println("O candidato " + candidato + " foi selecionado para a vaga.");
                candidatosSelecionados++;
            }
            candidatosAtual++;
        }

    }

    static double valorPretendido () {
        return ThreadLocalRandom.current().nextDouble(1800,2200);
    }

    static void analisarCandidato (double salarioPretendido) {
        if (salarioPretendido < 2000) 
            System.out.println("Ligar para o candidato.");
        else if (salarioPretendido == 2000)
            System.out.println("Ligar para o candidato com contra proposta.");
        else 
            System.out.println("Aguardando o resultado dos demais candidatos.");
    }    

}
