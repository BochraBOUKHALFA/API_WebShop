pipeline {
    agent any
    stages
   {

        stage('checkout')
        {
          steps
           {
                git branch: 'main',
                credentialsId: 'Bochra',
                url: 'https://github.com/bouchrasource/API_WebShop.git'
           }
        }

        stage('test')
       {
               steps
            {
               bat 'python test.py'
            }
       }

        stage('build')
       {
            steps
            {
               bat 'python setup.py sdist'
            }
       }

       stage('archive')
       {
           steps
           {
                bat 'rename dist\\PycharmProjects-0.1.tar.gz PycharmProjects-%BUILD_NUMBER%.tar.gz'
               archiveArtifacts artifacts: 'dist\\PycharmProjects-*.tar.gz', followSymlinks: false
           }
       }
   }
}
