# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vote'
        db.create_table(u'votein_server_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voter_ID', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('voteType', self.gf('django.db.models.fields.CharField')(default='Up', max_length=2)),
        ))
        db.send_create_signal(u'votein_server', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Vote'
        db.delete_table(u'votein_server_vote')


    models = {
        u'votein_server.vote': {
            'Meta': {'object_name': 'Vote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voteType': ('django.db.models.fields.CharField', [], {'default': "'Up'", 'max_length': '2'}),
            'voter_ID': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['votein_server']