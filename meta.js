const fs = require('fs')

module.exports = {
  prompts: {
    name: {
      type: 'string',
      required: true,
      message: 'Project name'
    },
    description: {
      type: 'string',
      required: false,
      message: '',
      default: 'My Fsquare project'
    },
    author: {
      type: 'string',
      message: 'Author'
    },
  },
  skipInterpolation: "frontend/**/*.vue",
	complete: (data, {chalk}) => {
    fs.rename(`${data.destDirName}/__project__`, `${data.destDirName}/${data.name}`, (err) => {
      if (err) {
        console.log(err);
      }
    });
		console.log(chalk.green('\nProject created \\o/!'));
		msg = `\n${chalk.bold('To get started:')}
    ${chalk.blueBright(`
 cd ${data.destDirName}
 follow the instructions on README.md`)}`;
		console.log(msg);
	}
};
