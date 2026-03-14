pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/aayush-bajpai/quiz_master.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                cd /home/ubuntu/quiz_master
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         sh '''
        //         cd /home/ubuntu/quiz_master
        //         source venv/bin/activate
        //         python manage.py test
        //         '''
        //     }
        // }

        // stage('Migrate Database') {
        //     steps {
        //         sh '''
        //         cd /home/ubuntu/quiz_master
        //         source venv/bin/activate
        //         python manage.py migrate
        //         '''
        //     }
        // }

        stage('Collect Static') {
            steps {
                sh '''
                cd /home/ubuntu/quiz_master
                source venv/bin/activate
                python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Restart Services') {
            steps {
                sh '''
                sudo supervisorctl restart guni:*
                sudo systemctl restart nginx
                '''
            }
        }

    }
}
