#!/usr/bin/env python3

import os

basic_conf = [{
    'question': 'Basic configurations\n\n\nHow to create kubectl completion? \n',
    'answer': 'echo "source <(kubectl completion bash)" >> ~/.bashrc',
    'obs': 'first obs',
    'link': 'http://google.com \n',
    },
    {
    'question': 'How to reload .bashrc ? \n',
    'answer': 'source ~/.bashrc',
    'obs': '',
    'link': '',
    },
    {
    'question': 'How to create an alias to kubectl ? \n',
    'answer': 'alias k=kubectl',
    'obs': '',
    'link': '',
    },
    {
    'question': 'How to see an specific namespace ? \n',
    'answer': 'k -n namespace',
    'obs': '',
    'link': '',
    },
    {
    'question': 'How to export a pod config to a yaml file ? \n',
    'answer': 'k get pod name -o yaml --export > file.yml',
    'obs': '',
    'link': '',
    },
    {
    'question': 'How to export a deployment config to a yaml file ? \n',
    'answer': 'k get deployment name -o yaml --export > file.yml',
    'obs': '',
    'link': '',
    },
    {
    'question': 'How to force a replace using a file ? \n',
    'answer': 'k replace -f file.yml --force',
    'obs': '',
    'link': '',
    },
    {
    'question': 'How to set configuration context ? \n',
    'answer': 'k config use-context name',
    'obs': '',
    'link': '',
    },
    {
    'question': 'How to get elevated privileges on exam ? \n',
    'answer': 'sudo -i',
    'obs': '',
    'link': '',
    }
]    

core_concepts = [{
    'question': 'Core Concepts - 13% \n\n\nWhat are the possible values for pod phase ? \n',
    'answer': 'pending, running, succeeded, failed, unknown',
    'obs': '',
    'link': '',
    },
    {
    'question': 'What are the types of API versioning\n',
    'answer': 'alpha, beta, stable',
    'obs': 'Alpha level:  The version names contain alpha (e.g. v1alpha1).\n Beta level: The version names contain beta (e.g. v2beta3)\n Stable level: The version name is vX where X is an integer.\n ',
    'link': 'https://kubernetes.io/docs/concepts/overview/kubernetes-api/',
    },
    {
    'question': 'How to see all APIs enabled? \n ',
    'answer': 'k api-versions',
    'obs': '',
    'link': '',
    },
    {
    'question': 'How to enable API groups?',
    'answer': '--runtime-config',
    'obs': 'enable: --runtime-config=batch/v2alpha1\n disable: --runtime-config=batch/v1=false\n',
    'link': 'https://kubernetes.io/docs/concepts/overview/kubernetes-api/',
    }
]


multi_container = [{
    'question': 'Multi-Container Pods - 10%\n\n\n What are the Multi-Container Pod design patterns \n?',
    'answer': 'ambassador, adapter, sidecare',
    'obs': '',
    'link': '',
    },
    {
    'question': 'Explain ambassor: \n',
    'answer': 'ambassor is',
    'obs': '',
    'link': '',
    },
    {
    'question': 'Explain adapter:',
    'answer': 'adapter is',
    'obs': '',
    'link': '',
    },
    {
    'question': 'Explain sidecare:',
    'answer': 'sidecare is',
    'obs': '',
    'link': '',
    }
]


pod_design = [{      
    'question': 'Pod Design - 20%\n\n\n How to set a label ?',
    'answer': 'set label',
    'obs': '',
    'link': '',
    },  
]

config = [{      
    'question': 'Configuration - 18%\n\n\n bla bla bla ?',
    'answer': 'bla',
    'obs': '',
    'link': '',
    },  
]

observability = [{      
    'question': 'Observability - 18%\n\n\n bla bla bla ?',
    'answer': 'bla',
    'obs': '',
    'link': '',
    },  
]

networking = [{      
    'question': 'Services & Networking - 13%\n\n\n bla bla bla ?',
    'answer': 'bla',
    'obs': '',
    'link': '',
    },  
]



def exec_choose(question):
    questions = question
    cq = 0
    for q in questions:
        if input(q['question']) == q['answer']:
            cq += 1
            print("correct \n")
            print(q['obs'])
            print("\n")
            print(q['link'])
            input('go to next? press <enter>\n')
            os.system("clear")
        else:
            print("incorrect \n")
            print("The correct is: {}" .format(q['answer']))
            print(q['obs'])
            print("\n")
            print(q['link'])
            input('go to next? press <enter>\n')
            os.system("clear")

    media = (cq / len(questions) * 100)
    print('sua media foi: {:.2f}'.format(media))

def main():
    while True:
        choose = input("""Choose one option to practice: \n
                         1) Basic configurations\n 
                         2) Core Concepts 13%\n 
                         3) Multi-Container Pods - 10%\n 
                         4) Pod Design - 20%\n
                         5) Configuration - 18%\n
                         6) Observability - 18%\n
                         7) Services & Networking - 13%\n
                         8) Exit\n
                       """)
        if choose == "1":
            exec_choose(basic_conf)
        elif choose == "2":
            exec_choose(core_concepts)
        elif choose == "3":
            exec_choose(multi_container)
        elif choose == "4":
            exec_choose(pod_design)
        elif choose == "5":
            exec_choose(config)
        elif choose == "6":
            exec_choose(observability)
        elif choose == "7":
            exec_choose(networking)
        elif choose == "8":
            break
        else:
            print("option not found")
            os.system("clear")

if __name__ == '__main__':
    main()