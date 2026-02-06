pipeline {
  agent any

  stages {
    stage('Info') {
      steps {
        sh '''
          echo "=== WHOAMI ==="
          whoami || true
          echo "=== PWD ==="
          pwd
          echo "=== Docker version ==="
          docker --version
          echo "=== Compose version ==="
          docker-compose version
        '''
      }
    }

   stage('Deploy (compose-project)') {
  steps {
    sh '''
      set -euxo pipefail
      cd /work/compose-project

      docker-compose pull
      docker-compose down --remove-orphans || true
      docker-compose up -d --build --force-recreate
      docker-compose ps
    '''
  }
}
