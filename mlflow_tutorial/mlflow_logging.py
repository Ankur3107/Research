import mlflow
import git, os



    
    
class TensorflowAutoLogging():
    
    def __init__(self, experiment_name, run_name, step_feq):
        import mlflow.tensorflow
        mlflow.tensorflow.autolog(step_feq)
        mlflow.set_experiment(experiment_name)
        mlflow.set_tag('mlflow.runName',run_name)
        
    def set_git_params(self, working_dir):
        
        git_info = self.__get_git_commit(working_dir)
        basic_config = {
            'mlflow.source.git.repoURL':git_info[0],
            'mlflow.source.git.branch':git_info[1],
            'mlflow.source.git.commit':git_info[2]
        }
        mlflow.set_tags(basic_config)
        
    def set_notes(self, note_str):
        mlflow.set_tag('mlflow.note.content',note_str)

    def set_other_params(self, params):
        mlflow.log_params(params)
        
    def stop_logging(self):
        mlflow.tracking.MlflowClient().set_terminated(mlflow.active_run().info.run_uuid)
        
    def __get_git_commit(self, path):
        try:
            import git
        except ImportError as e:
            _logger.warning(
                "Failed to import Git (the Git executable is probably not on your PATH),"
                " so Git SHA is not available. Error: %s", e)
            return None
        try:
            if os.path.isfile(path):
                path = os.path.dirname(path)
            repo = git.Repo(path, search_parent_directories=True)

            return (repo.working_dir, repo.active_branch.name, repo.head.commit.hexsha)
        except (git.InvalidGitRepositoryError, git.GitCommandNotFound, ValueError, git.NoSuchPathError):
            return (None, None, None)
    