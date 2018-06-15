#!/usr/bin/env python3

import os

basic_conf = [{
    'question': 'Basic configurations\n\n\nHow to create kubectl completion? \n',
    'answer': 'echo "source <(kubectl completion bash)" >> ~/.bashrc',
    'obs': '',
    'link': '',
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
    },
    {
    'question': 'What are the pods controllers?\n',
    'answer': 'deployment, statefulset, daemonset',
    'obs': '',
    'link': 'https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/',
    },
    {
    'question': 'What are the Container probes types ?\n',
    'answer': 'ExecAction, TCPSockAction, HTTPGetAction',
    'obs': '\nExecAction: Executes a specified command inside the Container. The diagnostic is considered successful if the command exits with a status code of 0. \n TCPSocketAction: Performs a TCP check against the Container’s IP address on a specified port. The diagnostic is considered successful if the port is open. \n HTTPGetAction: Performs an HTTP Get request against the Container’s IP address on a specified port and path. The diagnostic is considered successful if the response has a status code greater than or equal to 200 and less than 400. \n',
    'link': 'https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/',
    },
    {
    'question': 'Each probe has one of three results, what is this results? \n',
    'answer': 'Success, Failure, Unknown',
    'obs': 'Success: The Container passed the diagnostic.\n Failure: The Container failed the diagnostic. \n Unknown: The diagnostic failed, so no action should be taken.\n',
    'link': 'https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/',
    },
    {
    'question': 'The kubelet can optionally perform and react to two kinds of probes on running Containers, what are? \n',
    'answer': 'livenessProbe, readinessProbe',
    'obs': '\nlivenessProbe: Indicates whether the Container is running. If the liveness probe fails, the kubelet kills the Container, and the Container is subjected to its restart policy. If a Container does not provide a liveness probe, the default state is Success.\n readinessProbe: Indicates whether the Container is ready to service requests. If the readiness probe fails, the endpoints controller removes the Pod’s IP address from the endpoints of all Services that match the Pod. The default state of readiness before the initial delay is Failure. If a Container does not provide a readiness probe, the default state is Success\n',
    'link': 'https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/',
    },
    {
    'question': 'What are the  possible values to a restartPolicy ? \n',
    'answer': 'Always, OnFailure, and Never',
    'obs': '\nThe default value is Always. restartPolicy applies to all Containers in the Pod. restartPolicy only refers to restarts of the Containers by the kubelet on the same node. Exited Containers that are restarted by the kubelet are restarted with an exponential back-off delay (10s, 20s, 40s …) capped at five minutes, and is reset after ten minutes of successful execution. As discussed in the Pods document, once bound to a node, a Pod will never be rebound to another node\n',
    'link': 'https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/',
    },
    {
    'question': 'Pod lifetime, What are the Three types of controllers available? \n',
    'answer': 'Job, ReplicationController, ReplicaSet, or Deployment and DaemonSet \n',
    'obs': 'Use a Job for Pods that are expected to terminate, for example, batch computations. Jobs are appropriate only for Pods with restartPolicy equal to OnFailure or Never.\n Use a ReplicationController, ReplicaSet, or Deployment for Pods that are not expected to terminate, for example, web servers. ReplicationControllers are appropriate only for Pods with a restartPolicy of Always.\n Use a DaemonSet for Pods that need to run one per machine, because they provide a machine-specific system service.\n',
    'link': 'https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/',
    },
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
    print('Your Result: {:.2f}'.format(media))

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