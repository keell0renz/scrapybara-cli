import typer

def main(instance_type: str = "small"):
    """
    Run the CLI-based computer agent, powered by Scrapybara and Anthropic!
    
    Args:
        instance_type: Size of the instance. Must be one of: "small", "medium", "large"
    """
    if instance_type not in ["small", "medium", "large"]:
        raise ValueError('instance_type must be one of: "small", "medium", "large"')
    
    print(instance_type)
    

if __name__ == "__main__":
    typer.run(main)