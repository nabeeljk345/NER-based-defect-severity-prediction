pipeline{
            agent any
            stages{
            stage('Test Case Generation'){
                steps{
                        sh 'python test-case-generator.py'
                        }
                        }
            stage('Run Automated Tests'){
                 steps{
                        sh 'pytest --html=report.html'
                        }
                        }

            stage('Defect Prediction'){
                  steps{
                         sh 'python defect-predictor.py'
                         }
                         }
            stage('Notify Team'){
                    steps{
                           sh 'python send_notification.py'
                           }
                           }
                           }
                     }