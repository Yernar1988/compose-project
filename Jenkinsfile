pipeline {
  options { ansiColor("xterm") }

  agent any

  stages {
    stage("Sanity check Jenkinsfile") {
      steps {
        sh """
          set -eu
          if grep -nE "(^|[^a-zA-Z])(git commit|git push|cat > Jenkinsfile|<<\x27EOF\x27)" Jenkinsfile; then
            echo "ERROR: Jenkinsfile contains pasted terminal commands. Fix it." >&2
            exit 2
          fi
        """
      }
    }

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
          docker-compose pull || true
          docker-compose up -d --build
          docker-compose ps
        '''
      }
    }
  }
}
